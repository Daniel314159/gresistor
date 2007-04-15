Summary:	Resistor color code calculator
Name:		gresistor
Version:	0.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.minipop.org/progs/gresistor/%{name}-%{version}.tar.gz
# Source0-md5:	d8e5d3a4a5f73f081a4892b220b0f178
Patch0:		%{name}-desktop.patch
URL:		http://minipop.org/index.php?file=gresistor
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	python-pygtk-glade
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
To allow for identification, resistors are usually marked with colored
bands. Often refereed to as color codes, these markings are indicative
of their resistance, tolerance and temperature coefficient. gResistror
is a great program that will help you translate a resistor color codes
into a readable value. All you have to do is watch the colors on the
resistor and then enter them in the program. As you enter you'll see
that the resistor value is changing according to the selected color.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__python} setup.py install \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT

install pixmaps/icon.png $RPM_BUILD_ROOT%{_pixmapsdir}/gresistor.png

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gresistor
%{py_sitescriptdir}/*.py[co]
%{py_sitescriptdir}/gresistor-*.egg-info
%{_desktopdir}/gresistor.desktop
%{_datadir}/gresistor
%{_pixmapsdir}/gresistor.png