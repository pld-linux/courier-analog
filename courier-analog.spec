%include	/usr/lib/rpm/macros.perl
Summary:	Courier log analyzer
Summary(pl.UTF-8):	Analizator logów couriera
Name:		courier-analog
Version:	0.17
Release:	1
License:	GPL v3 with OpenSSL exception
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	71107e63edf6fcfd36127821754edbaa
URL:		http://www.courier-mta.org/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The courier-analog script generates log summaries for the Courier mail
server.

%description -l pl.UTF-8
Courier-analog to skrypt, który generuje podsumowanie logów dla
couriera.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README courier-analog.html manpage.css
%attr(755,root,root) %{_bindir}/courier-analog
%{_mandir}/man8/courier-analog.8*
