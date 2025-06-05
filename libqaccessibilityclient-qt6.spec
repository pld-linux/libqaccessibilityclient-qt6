#
# Conditional build:
%bcond_with	tests	# test suite

%define		kf_ver	5.91.0
%define		qt_ver	6.5.0
%define		kfname	libqaccessibilityclient
Summary:	Accessibilty tools helper library
Summary(pl.UTF-8):	Biblioteka pomocnicza dla narzędzi wspomagających dostępność
Name:		libqaccessibilityclient-qt6
Version:	0.6.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries
# TODO:
#Source0:	https://github.com/KDE/libqaccessibilityclient/archive/v%{version}/%{kfname}-%{version}.tar.gz
Source0:	https://github.com/KDE/libqaccessibilityclient/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	12f90db3f6f855ea898fa87a7569a12f
URL:		https://github.com/KDE/libqaccessibilityclient
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6DBus-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
%{?with_test:BuildRequires:	Qt6Test-devel >= %{qt_ver}}
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6DBus >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is used when writing accessibility clients such as screen
readers. It comes with some examples demonstrating the API. These
small helpers may be useful when testing accessibility. One of them
writes all accessibility interfaces an application provides as text
output. The other, more advanced application shows a tree of objects
and allows some interaction and exploration.

%description -l pl.UTF-8
Ta biblioteka jest używana przy pisaniu klientów usług dostępności,
takich jak czytniki ekranów. Jest dostarczana z przykładami
demonstrującymi API. Te małe programy mogą być przydatne przy
testowaniu dostępności. Jeden z nich wypisuje wszystkie interfejsy
dostępności zapewniane przez aplikację jako wyjście tekstowe. Inna,
bardziej zaawansowana aplikacja, pokazuje drzewo obiektów i pozwala na
pewną interakcję i eksplorowanie.

%package devel
Summary:	Header files for libqaccessibilityclient library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libqaccessibilityclient
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qt_ver}
Requires:	Qt6Widgets-devel >= %{qt_ver}

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
%attr(755,root,root) %{_libdir}/libqaccessibilityclient-qt6.so.*.*
%ghost %{_libdir}/libqaccessibilityclient-qt6.so.0
%{_datadir}/qlogging-categories6/libqaccessibilityclient.categories

%files devel
%defattr(644,root,root,755)
%{_libdir}/libqaccessibilityclient-qt6.so
%{_includedir}/QAccessibilityClient6
%{_libdir}/cmake/QAccessibilityClient6
