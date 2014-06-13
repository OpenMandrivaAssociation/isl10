%define major	10
%define libname	%mklibname isl %{major}
%define devname	%mklibname isl -d

Summary:	Old version of the isl Integer Set Library
Name:		isl10
Version:	0.12.2
Release:	2
License:	MIT
Group:		System/Libraries
Url:		git://repo.or.cz/isl.git
Source0:	ftp://gcc.gnu.org/pub/gcc/infrastructure/isl-%{version}.tar.bz2
# See http://gcc.gnu.org/bugzilla/show_bug.cgi?id=58012
Patch0:		isl-no-iostream.patch
BuildRequires:	gmp-devel

%description
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

This is an old version provided for compatibility with legacy applications
only.

%package -n	%{libname}
Summary:	Integer Set Library
Group:		System/Libraries

%description -n	%{libname}
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, computing the lexicographic
minimum using parametric integer programming, coalescing and parametric
vertex enumeration.

It also includes an ILP solver based on generalized basis reduction,
transitive closures on maps (which may encode infinite graphs),
dependence analysis and bounds on piecewise step-polynomials.

This is an old version provided for compatibility with legacy applications
only.

%package -n	%{devname}
Summary:	Development files for the isl Integer Set Library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}isl-static-devel < 0.11.1-3

%description -n	%{devname}
Header files for the isl Integer Set Library.

This is an old version provided for compatibility with legacy applications
only.

%prep
%setup -q -n isl-%{version}
%apply_patches
autoreconf -fi

%build
%configure
%make

%check
# All tests must pass
make check

%install
%makeinstall_std

# (tpg) not needed ?
rm -rf %{buildroot}%{_libdir}/*%{name}*-gdb.py

# No development files for compat packages
rm -rf	%{buildroot}%{_libdir}/libisl.so \
	%{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/pkgconfig \
	%{buildroot}%{_libdir}/libisl.a

%files -n %{libname}
%{_libdir}/libisl.so.%{major}*

#files -n %{devname}
#{_libdir}/libisl.so
#{_includedir}/*
#{_libdir}/pkgconfig/*.pc

