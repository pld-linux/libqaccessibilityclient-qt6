%define		kfname	libqaccessibilityclient
Summary:	libqaccessibilityclient-qt6
Name:		libqaccessibilityclient-qt6
Version:	0.6.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	https://github.com/KDE/%{kfname}/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	12f90db3f6f855ea898fa87a7569a12f
URL:		https://github.com/KDE/libqaccessibilityclient
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is used when writing accessibility clients such as screen
readers. It comes with some examples demonstrating the API. These
small helpers may be useful when testing accessibility. One of them
writes all accessibiliy interfaces an application provides as text
output. The other, more advanced application shows a tree of objects
and allows some interaction and exploration.

%package devel
Summary:	Header files for qalculate library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki qalculate
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake \
		-B build \
		-G Ninja \
		%{!?with_tests:-DBUILD_TESTING=OFF} \
		-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
		-DBUILD_WITH_QT6=ON

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%ghost %{_libdir}/libqaccessibilityclient-qt6.so.0
%attr(755,root,root) %{_libdir}/libqaccessibilityclient-qt6.so.*.*
%{_datadir}/qlogging-categories6/libqaccessibilityclient.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/QAccessibilityClient6
%{_libdir}/cmake/QAccessibilityClient6
%{_libdir}/libqaccessibilityclient-qt6.so
