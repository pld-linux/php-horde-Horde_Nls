# TODO:
# - use system locale dir
%define		status		stable
%define		pearname	Horde_Nls
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - This package provides Native Language Support (NLS)
Name:		php-horde-Horde_Nls
Version:	1.1.6
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	644a692ce0d845665d0b6f0ab58a3955
URL:		https://github.com/horde/horde/tree/master/framework/Nls/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php(geoip)
Suggests:	php-pear-Net_DNS2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Net/DNS2.*)

%description
Provide common methods for handling language data, timezones, and
hostname->country lookups.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Nls.php
%{php_pear_dir}/Horde/Nls
%{php_pear_dir}/data/Horde_Nls
