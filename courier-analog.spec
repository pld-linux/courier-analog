Summary:	Courier log analyzer
Summary(pl.UTF-8):   Analizator logów couriera
Name:		courier-analog
Version:	0.12
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/courier/%{name}-%{version}.tar.bz2
# Source0-md5:	020ad544f55de811b7f1eca40343f9d2
URL:		http://www.courier-mta.org/
BuildRequires:	perl
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
%configure

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README courier-analog.html manpage.css
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
