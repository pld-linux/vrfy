Summary:	vrfy - a tool to verify email addresses and mailing lists
Summary(pl.UTF-8):   vrfy - narzędzie służące do weryfikacji adresów pocztowych
Name:		vrfy
Version:	990522
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.nikhef.nl/pub/network/%{name}_%{version}.tar.Z
# Source0-md5:	57144a8dc9b877f31b86c95d5152425f
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'vrfy' is a tool to verify email addresses and mailing lists. In its
simplest form it takes an address "user@domain", figures out the MX
hosts for "domain", and issues the SMTP command VRFY at the primary MX
host (optionally all), or at "domain" itself if no MX hosts exist.
Without "domain" it goes to "localhost". More complex capabilities
are: recursively expanding forward files or mailing lists, and
detecting mail forwarding loops. Full-blown RFC822 address
specifications are understood. Syntax checking can be carried out
either locally or remotely. Various options are provided to exploit
alternative protocol suites if necessary, and to print many forms of
verbose output. Obvious limitations exist, but on average it works
pretty well. Needless to say you need Internet (nameserver and SMTP)
access. See the man page and the extensive documentation in the source
for further details.

%description -l pl.UTF-8
'vrfy' to narzędzie służące weryfikacji adresów e-mail i list
mailowych. W najprostszej formie przyjmuje adres w postaci
"użytkownik@domena", sprawdza hosty MX dla "domeny" i wysyła polecenie
SMTP VRFY do głównego hosta MX (opcjonalnie do wszystkich) lub samej
"domeny", jeśli nie istnieje wpis MX. Bez "domeny" łączy się z hostem
"localhost". Bardziej zaawansowane możliwości to: rekurencyjne
rozwiązywanie plików forward i list mailowych oraz wykrywanie pętli
przekazywania poczty. Rozumiana jest pełna specyfikacja adresów
RFC822. Kontrola składni może być przeprowadzana lokalnie lub zdalnie.
Dostępne są różne opcje do wykorzystywania w razie potrzeby
alternatywnych protokołów i wypisywania różnych postaci obszernego
wyjścia. Istnieją oczywiste ograniczenia, ale przeważnie narzędzie
działa w miarę dobrze. Oczywiście wymagane jest łącze do Internetu
(serwera nazw i SMTP). Więcej szczegółów na stronie manuala oraz w
obszernej dokumentacji w kodzie źródłowym.

%prep
%setup -q -c %{name}

%build
%{__make} \
	CFLAGS="%{rpmcflags} -D_BSD_SOURCE" \
	LDFLAGS="%{rpmldflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install vrfy $RPM_BUILD_ROOT%{_bindir}/vrfy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vrfy
