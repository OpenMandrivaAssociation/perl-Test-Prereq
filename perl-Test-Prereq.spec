%define module  Test-Prereq
%define name    perl-%{module}
%define version 1.037
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Check if Makefile.PL has the right pre-requisites
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Info)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Test::Builder::Tester)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
The prereq_ok() function examines the modules it finds in blib/lib/,
blib/script, and the test files it finds in t/ (and test.pl). It figures out
which modules they use, skips the modules that are in the Perl core, and
compares the remaining list of modules to those in the PREREQ_PM section of
Makefile.PL.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
# this test rely on network to fetch data from CPAN
rm -f t/get_from_prereqs.t
perl -pi -e 's/get_from_prereqs.t//' t/test_manifest
%{__make} test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{perl_vendorlib}/Test
%{_mandir}/*/*


