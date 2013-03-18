%define oname libmad
%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	High-quality MPEG Audio Decoder
Name:		mad
Version:	0.15.1b
Release:	16
License:	GPLv2+
Group:		Sound
URL:		http://www.underbit.com/products/mad/
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

%package -n	%{develname}
Summary:	Development tools for programs which will use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	zlib-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package includes the header files and static libraries
necessary for developing programs using the %{name} library.

If you are going to develop programs which will use the %{name} library
you should install this.


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0
%patch1 -p1 -b .am113~
%patch2 -p1 -b .arm_bits
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

%files -n %{develname}
%doc COPY* README TODO CHANGES CREDITS
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*.h


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.15.1b-12
+ Revision: 666355
- mass rebuild

  + Per Ã˜yvind Karlsen <peroyvind@mandriva.org>
    - clean out old junk...

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.1b-10mdv2011.0
+ Revision: 606620
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.1b-9mdv2010.1
+ Revision: 523237
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.15.1b-8mdv2010.0
+ Revision: 426052
- rebuild

* Sun Jul 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.15.1b-7mdv2009.0
+ Revision: 232176
- added P0 to fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.15.1b-5mdv2008.1
+ Revision: 170974
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.1b-4mdv2008.1
+ Revision: 101743
- new devel name
- update license tag

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot


* Sun Jan 14 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.1b-4mdv2007.0
+ Revision: 108695
- Import mad

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 0.15.1b-4mdv2007.1
- rebuild

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.15.1b-4mdk
- Rebuild

* Wed Feb 09 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.15.1b-3mdk
- multiarch

* Fri Oct 01 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.15.1b-2mdk
- lib64 fixes to pkgconfig files

* Tue May 11 2004 Götz Waschk <waschk@linux-mandrake.com> 0.15.1b-1mdk
- spec fix
- don't libtoolize
- fix source URL
- New release 0.15.1b

