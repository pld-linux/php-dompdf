# TODO
# - external php-font-lib
# - external php-tcpdf
%define		pkgname	dompdf
%define		php_min_version 5.2.7
Summary:	HTML to PDF converter
Name:		php-%{pkgname}
Version:	0.6.2
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	https://github.com/dompdf/dompdf/releases/download/v%{version}/dompdf-%{version}.zip
# Source0-md5:	06c265913be9c0935c4f607617a7af0f
Patch0:		config.patch
URL:		http://dompdf.github.io/
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(dom)
Requires:	php(gd)
Requires:	php(iconv)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(xml)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear  dompdf_config.inc.php .*Font_Binary_Stream.php

# exclude optional php dependencies
%define		_noautophp	php-curl php-pgsql php.*pgsql

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%define		_appdir			%{php_data_dir}/%{pkgname}
%define		_sysconfdir		/etc/%{pkgname}

%description
dompdf is an HTML to PDF converter. At its heart, dompdf is (mostly)
CSS 2.1 compliant HTML layout and rendering engine written in PHP. It
is a style-driven renderer: it will download and read external
stylesheets, inline style tags, and the style attributes of individual
HTML elements. It also supports most presentational HTML attributes.

%prep
%setup -qc
mv %{pkgname}/* .
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir}}
cp -a dompdf.php load_font.php include lib $RPM_BUILD_ROOT%{_appdir}
cp -p dompdf_config.inc.php $RPM_BUILD_ROOT%{_sysconfdir}
ln -s %{_sysconfdir}/dompdf_config.inc.php $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a www/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dompdf_config.inc.php
%{_appdir}
%{_examplesdir}/%{name}-%{version}
