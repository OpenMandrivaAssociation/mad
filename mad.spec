%define oname libmad
%define major 0
%define libname %mklibname mad %{major}
%define develname %mklibname -d mad

Summary:	High-quality MPEG Audio Decoder
Name:		mad
Version:	0.15.1b
Release:	13
License:	GPLv2+
Group:		Sound
URL:		http://www.underbit.com/products/mad/
Source0:	http://prdownloads.sourceforge.net/mad/%oname-%version.tar.bz2
Source2:	mad.pc
Patch0:		libmad-no_-fforce-mem.diff

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

%package -n %{libname}
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

%package -n %{develname}
Summary:	Development tools for programs which will use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	zlib-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}
Obsoletes:	%mklibname -d mad 0

%description -n %{develname}
This package includes the header files and static libraries
necessary for developing programs using the %{name} library.
 
If you are going to develop programs which will use the %{name} library
you should install this.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0
rm -f configure
touch NEWS AUTHORS ChangeLog
autoreconf -fis

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -m644 %{SOURCE2} %{buildroot}%{_libdir}/pkgconfig
sed -e 's,/lib$,/%{_lib},' %{buildroot}%{_libdir}/pkgconfig/mad.pc
sed -e "s/VERSION/%{version}/" %{buildroot}%{_libdir}/pkgconfig/mad.pc

%multiarch_includes %{buildroot}%{_includedir}/mad.h

%find_lang %{name}

%files -n %{libname}
%{_libdir}/libmad.so.%{major}*

%files -n %develname
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
%{multiarch_includedir}/*.h
