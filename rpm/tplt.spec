%global debug_package %{nil}
%UNPACKAGED_TRACK%

Summary:	%PFX%%VMOD%
Name:		%PFX%%VMOD%
Version:	%VRT%.%VER%
Release:	1%{?dist}
License:	See original VMOD source license file.

Source:	    vmod.tar.gz

Requires: varnish >= %VARNISH_VER%, varnish < %VARNISH_VER_NXT%%REQUIRE%

%description
Packed by vmod-packager

%prep
rm -rf %{buildroot}
%setup -q -n src

%build
./__vmod-package_config.sh
%make_build


%install
%make_install
find %{buildroot}/%{_libdir}/ -name '*.la' -exec rm -f {} ';'
find %{buildroot}/%{_libdir}/ -name '*.a' -exec rm -f {} ';'

%check
%TEST%

%files
%{_libdir}/varnish/vmods/*.so
%FILES_DATADIR%
%FILES_MAN%

%changelog
* %TIME% %PFX%%VMOD% <example@localhost> - %VRT%.%VER%
- Packaged by vmod-packager