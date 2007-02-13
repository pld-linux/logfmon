# TODO:	initscript, default configuration suitable for PLD
Summary:	logfmon - log file monitoring daemon
Summary(pl.UTF-8):	logfmon - demon monitorujący pliki logów
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

%description -l pl.UTF-8
Demon logfmon monitoruje zestaw plików sysloga i porównuje każdy nowy
wpis z regułami zdefiniowanymi w swoim pliku konfiguracyjnym. Każda
reguła może być porównywana z linią z jednego lub wielu plików. W
zależności od reguły może być wykonywana komenda lub wpis może być
ignorowany. Wszystkie niedopasowane linie są zbierane i wysyłane
pocztą, domyślnie co 15 minut lub co okres czasu zdefiniowany w pliku
konfiguracyjnym.

Wiadomości mogą być także zbierane w konteksty i przekazywane potokiem
do komendy po znalezieniu ostatniej wiadomości lub osiągnięciu ich
liczby - więcej szczegółów w logfmon.conf(5) na temat tej opcji.

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
