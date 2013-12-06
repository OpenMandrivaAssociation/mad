%define oname libmad
%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	High-quality MPEG Audio Decoder
Name:		mad
Version:	0.15.1b
Release:	21
License:	GPLv2+
Group:		Sound
Url:		http://www.underbit.com/products/mad/
Source0:	http://prdownloads.sourceforge.net/mad/%{oname}-%{version}.tar.bz2
Source2:	mad.pc.bz2
Patch0:		libmad-no_-fforce-mem.diff
Patch1:		libmad-automake-1.13.patch
Patch2:		libmad-0.15.1b-thumb2-fixed-arm.patch

%description
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2  extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II, 
and Layer III a.k.a. MP3) are fully implemented.

MAD does not yet support MPEG-2 multichannel audio (although it should 
be backward compatible with such streams) nor does it currently support AAC.

MAD has the following special features:
    * 24-bit PCM output
    * 100% fixed-point (integer) computation
    * completely new implementation based on the ISO/IEC standards

%package -n	%{libname}
Summary:	High-quality MPEG Audio Decoder
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n	%{libname}
MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1
and the MPEG-2  extension to Lower Sampling Frequencies, as well as the
so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II, 
and Layer III a.k.a. MP3) are fully implemented.

MAD does not yet support MPEG-2 multichannel audio (although it should
be backward compatible with such streams) nor does it currently support AAC.

MAD has the following special features:
    * 24-bit PCM output
    * 100% fixed-point (integer) computation
    * completely new implementation based on the ISO/IEC standards

%package -n	%{devname}
Summary:	Development tools for programs which will use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the header files and static libraries
necessary for developing programs using the %{name} library.

If you are going to develop programs which will use the %{name} library
you should install this.


%prep
%setup -qn %{oname}-%{version}
%apply_patches
rm -f configure
touch NEWS AUTHORS ChangeLog
autoreconf -fis

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_libdir}/pkgconfig
bzip2 -cd %{SOURCE2} | sed -e 's,/lib$,/%{_lib},' >%{buildroot}%{_libdir}/pkgconfig/mad.pc
perl -pi -e "s/0.14.2b/%{version}/" %{buildroot}%{_libdir}/pkgconfig/mad.pc

%files -n %{libname}
%doc COPYING
%{_libdir}/libmad.so.%{major}*

%files -n %{devname}
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h

