Name:		gxemul
Version:	0.6.0
Release:	%mkrel 2
License:	BSD
Group:		Emulators
Summary:	Instruction-level machine emulator
URL:		http://gavare.se/gxemul/
Source0:	http://gavare.se/gxemul/src/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libx11-devel

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
export CFLAGS="%{optflags} -finline-functions -O3"
./configure
%make

%install
rm -rf %{buildroot}
install -m755 gxemul -D %{buildroot}%{_bindir}/gxemul
install -m644 man/gxemul.1 -D %{buildroot}%{_mandir}/man1/gxemul.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE HISTORY README doc/* demos/
%{_bindir}/gxemul
%{_mandir}/man1/gxemul.1*
