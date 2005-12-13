# TODO:	initscript, default configuration suitable for PLD
Summary:	logfmon - log file monitoring daemon
Summary(pl):	logfmon - demon monitoruj±cy pliki logów
Name:		logfmon
Version:	0.7
Release:	0.1
License:	distributable
Group:		Daemons
Source0:	http://dl.sourceforge.net/logfmon/%{name}-%{version}.tar.gz
# Source0-md5:	f1bd697b140baef703f49fcc48b1a42c
Patch0:		%{name}-make-linux.patch
Patch1:		%{name}-conf.patch
URL:		http://logfmon.sourceforge.net/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The logfmon daemon monitors a set of syslog log files and matches each
new entry against the rules defined in it's configuration file. Each
rule may be tested against lines from a single file or from all files.
Depending on the rule, a command may be executed or the entry may be
ignored. All unmatched messages are batched together and mailed every
15 minutes, or whatever alternative time is specified in the
configuration file.

Messages may also be collected into contexts and piped to a command
after a final message is found or a number of messages is reached. See
logfmon.conf(5) for more details of this.

%description -l pl
Demon logfmon monitoruje zestaw plików sysloga i porównuje ka¿dy nowy
wpis z regu³ami zdefiniowanymi w swoim pliku konfiguracyjnym. Ka¿da
regu³a mo¿e byæ porównywana z lini± z jednego lub wielu plików. W
zale¿no¶ci od regu³y mo¿e byæ wykonywana komenda lub wpis mo¿e byæ
ignorowany. Wszystkie niedopasowane linie s± zbierane i wysy³ane
poczt±, domy¶lnie co 15 minut lub co okres czasu zdefiniowany w pliku
konfiguracyjnym.

Wiadomo¶ci mog± byæ tak¿e zbierane w konteksty i przekazywane potokiem
do komendy po znalezieniu ostatniej wiadomo¶ci lub osi±gniêciu ich
liczby - wiêcej szczegó³ów w logfmon.conf(5) na temat tej opcji.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

sed -i -e 's/gcc/%{__cc}/g;s/yacc/bison -y/' make-linux.sh

%build
./make-linux.sh "%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D logfmon $RPM_BUILD_ROOT%{_bindir}/logfmon
install -D logfmon.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/logfmon.conf.5
install -D logfmon.8 $RPM_BUILD_ROOT%{_mandir}/man8/logfmon.8
install -D logfmon.conf $RPM_BUILD_ROOT%{_sysconfdir}/logfmon.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[58]/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/logfmon.conf
