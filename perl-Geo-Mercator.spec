%define upstream_name    Geo-Mercator
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Compute Mercator Projection of latitude/longitude into meters
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Geo/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Computes Mercator Projection of input latitude/longitude coordinates (in
degrees) into (x, y) coordinates (as distances in meters) from the
meridian/equator. Also provides a method to convert back into latitude,
longitude.

Notes
    Use of Mercator projection on latitudes above/below +70/-70 degrees is
    strongly discouraged, due to the gross distortions of the projection.
    In fact, any use of the Mercator projection is strongly
    discouraged...but its the view we've all been programmed to see for 400
    years, so its genetic sense memory by now. And if its good enough for
    Google, its good enough for me.

    This module was developed primarily for graphic rendering purposes. The
    returned distance values *should not be used for navigational
    purposes*. They are only useful for certain mapping operations, e.g.,
    rendering a map to scale. For better approximations of actual
    distances, consider the Math::Trig manpage's great_circle_distance()
    function instead.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)

%{_mandir}/man3/*
%perl_vendorlib/*


