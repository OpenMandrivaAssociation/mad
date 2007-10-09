%define name 	mad
%define oname 	libmad
%define version 0.15.1b
%define release %mkrel 4
%define major  	0
%define lib_name %mklibname mad %{major}

Summary:	Libmad is a high-quality MPEG Audio Decoder
Name:		%{name}
Version:	%{version}
Release:	%{release}

Source0:	http://prdownloads.sourceforge.net/mad/%oname-%version.tar.bz2
Source2:	mad.pc.bz2
License:	GPL
Group:		Sound
URL:		http://www.underbit.com/products/mad/
BuildRoot:	%_tmppath/%name-%version-%release-root

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

%package -n %{lib_name}
Summary:        Libmad is a high-quality MPEG Audio Decoder
Group:          System/Libraries
Provides:       lib%{name} = %{version}-%{release}

%description -n %{lib_name}
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

%package -n %{lib_name}-devel
Summary:        Development tools for programs which will use the %{name} library
Group:          Development/C
Requires:	%{lib_name} = %{version}
Requires:	zlib-devel
Requires:	pkgconfig
Provides:       %{name}-devel = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Obsoletes: 	%{name}-devel

%description -n %{lib_name}-devel
The %{name}-devel package includes the header files and static libraries
necessary for developing programs using the %{name} library.
 
If you are going to develop programs which will use the %{name} library
you should install %{name}-devel.  You'll also need to have the %name
package installed.
 

%prep
%setup -q -n %oname-%version

%build
%define __libtoolize true
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall
%find_lang %{name}
mkdir -p %buildroot/%_libdir/pkgconfig
bzip2 -cd %SOURCE2 | sed -e 's,/lib$,/%{_lib},' >%buildroot/%_libdir/pkgconfig/mad.pc
perl -pi -e "s/0.14.2b/%version/" %buildroot/%_libdir/pkgconfig/mad.pc
%multiarch_includes %buildroot%{_includedir}/mad.h

%clean
rm -fr %buildroot

%post -n %{lib_name} -p /sbin/ldconfig
 
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
%_libdir/pkgconfig/*
%{_includedir}/*
%multiarch %{multiarch_includedir}/*.h


