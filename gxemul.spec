Name:		gxemul
Version:	0.6.2
Release:	1
License:	BSD
Group:		Emulators
Summary:	Instruction-level machine emulator
URL:		http://gavare.se/gxemul/
Source0:	http://gavare.se/gxemul/src/%{name}-%{version}.tar.gz
patch0:		gxemul-0.6.0.cstdlib.patch
BuildRequires:	pkgconfig(x11)

%description
GXemul is an experimental instruction-level machine emulator. Several
emulation modes are available. In some modes, processors and
surrounding hardware components are emulated well enough to let
unmodified operating systems (e.g. NetBSD) run as if they were running
on a real machine.

Currently supported processors include ARM, MIPS, PowerPC, and SuperH.

%prep
%setup -q
%patch0 -p1 -b .cstdlib

%build
# inlining should help for this kind of emulation project
export CFLAGS="%{optflags} -finline-functions -O3"
./configure
%make

%install
install -m755 gxemul -D %{buildroot}%{_bindir}/gxemul
install -m644 man/gxemul.1 -D %{buildroot}%{_mandir}/man1/gxemul.1

%files
%defattr(-,root,root)
%doc LICENSE HISTORY README doc/* demos/
%{_bindir}/gxemul
%{_mandir}/man1/gxemul.1*


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-2mdv2011.0
+ Revision: 611054
- rebuild

* Sun Feb 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 505886
- update to new 0.6.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Feb 10 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.4.7.1-1mdv2009.1
+ Revision: 339048
- new release: 0.4.7.1
- build with -O3
- spec cleanups

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.4.6.3-3mdv2009.0
+ Revision: 246773
- rebuild

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 0.4.6.3-1mdv2008.1
+ Revision: 177280
- update to new version 0.4.6.3

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 0.4.6.2-1mdv2008.1
+ Revision: 161824
- New version 0.4.6.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 24 2007 Gwenole Beauchesne <gbeauchesne@mandriva.org> 0.4.5.1-1mdv2008.0
+ Revision: 30683
- first mandriva linux package

