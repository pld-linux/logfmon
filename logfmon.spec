# TODO:	initscript, default configuration suitable for PLD
Summary:	logfmon - log file monitoring daemon
Summary(pl):	logfmon - demon monitorujacy pliki log�w
Name:		logfmon
Version:	0.4
Release:	0.1
License:	distributable
Group:		Daemons
Source0:	http://mesh.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	644459b7a211ae48009c8bd9a81e59ac
Patch0:		%{name}-make-linux.patch
Patch1:		%{name}-conf.patch
URL:		http://logfmon.sourceforge.net/
BuildRequires:	byacc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The logfmon daemon monitors a set of syslog log files and matches each
new entry against the rules defined in it's configuration file. Each
rule may be tested against lines from a single file or from all files.
Depend- ing on the rule, a command may be executed or the entry may be
ignored. All unmatched messages are batched together and mailed every
15 minutes, or whatever alternative time is specified in the
configuration file.

Messages may also be collected into contexts and piped to a command
after a final message is found or a number of messages is reached. See
logfmon.conf(5) for more details of this.

%description -l pl
Demon logfmon monitoruje zestaw plik�w sysloga i por�wnuje ka�dy nowy
wpis z regu�ami zdefiniowanymi w swoim pliku konfiguracyjnym. Ka�da
regu�a mo�e by� por�wnywana z lini� z jednego lub wielu plik�w. W
zale�no�ci od regu�y mo�e by� wykonywana komenda lub wpis mo�e by�
ignorowany. Wszystkie niedoasowane linie s� zbierane i wysy�ane
poczt�, domy�lnie co 15 minut lub co okres czasu zdefiniowany w pliku
konfiguracyjnym.

Wiadomo�ci mog� by� tak�e zbierane w konteksty i potokowane do komendy
po znalezieniu ostatniej wiadomo�ci lub osi�gni�ciu ich liczby -
wi�cej szczeg��w w logfmon.conf(5) na temat tej opcji.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

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
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/logfmon.conf