Summary:	'vrfy' is a tool to verify email addresses and mailing lists
Summary(pl):	'vrfy' to narzêdzie s³u¿±ce do weryfikacji adresów pocztowych
Name:		vrfy
Version:	990522
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.nikhef.nl/pub/network/%{name}_%{version}.tar.Z
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
pretty well. Needless to say you need internet (nameserver and SMTP)
access. See the man page and the extensive documentation in the source
for further details.

%description -l pl
'vrfy' to narzêdzie s³u¿±ce weryfikacji adresów pocztowych.

%prep
%setup -q -c %{name}

%build
%{__make} CFLAGS="%{rpmcflags} -D_BSD_SOURCE" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d   $RPM_BUILD_ROOT/%{_bindir}
install vrfy $RPM_BUILD_ROOT/%{_bindir}/vrfy

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/vrfy
