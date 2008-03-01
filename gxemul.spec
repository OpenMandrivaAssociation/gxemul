%define name	gxemul
%define version	0.4.6.3
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Emulators
Summary:	Instruction-level machine emulator
URL:		http://gavare.se/gxemul
Source0:	http://gavare.se/gxemul/src/%name-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdkversion} < 200700
BuildRequires:	X11-devel
%else
BuildRequires:	libx11-devel
%endif

%description
GXemul is an experimental instruction-level machine emulator. Several
emulation modes are available. In some modes, processors and
surrounding hardware components are emulated well enough to let
unmodified operating systems (e.g. NetBSD) run as if they were running
on a real machine.

Currently supported processors include ARM, MIPS, PowerPC, and SuperH.

%prep
%setup -q

%build
# inlining should help for this kind of emulation project
export CFLAGS="$RPM_OPT_FLAGS -finline-functions"
./configure
%make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m755 gxemul $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m644 man/gxemul.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE HISTORY README doc/* demos/
%{_bindir}/gxemul
%{_mandir}/man1/gxemul.*
