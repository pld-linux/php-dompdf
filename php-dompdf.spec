%define		pkgname	dompdf
%define		php_min_version 5.2.1
%include	/usr/lib/rpm/macros.php
Summary:	HTML to PDF converter
Name:		php-%{pkgname}
Version:	0.6.1
Release:	1
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	https://github.com/dompdf/dompdf/releases/download/v%{version}/dompdf-%{version}.zip
# Source0-md5:	7ac81b1a96d4311cd47d756b48d01de4
URL:		http://dompdf.github.io/
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(mbstring)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_pear  dompdf_config.inc.php
%define		_appdir			%{php_data_dir}/%{pkgname}

%description
dompdf is an HTML to PDF converter. At its heart, dompdf is (mostly)
CSS 2.1 compliant HTML layout and rendering engine written in PHP. It
is a style-driven renderer: it will download and read external
stylesheets, inline style tags, and the style attributes of individual
HTML elements. It also supports most presentational HTML attributes.

%prep
%setup -qc
mv %{pkgname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p *.php $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CONTRIBUTING.md
%{_appdir}
