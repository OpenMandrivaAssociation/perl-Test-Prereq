%define upstream_name    Test-Prereq
%define upstream_version 1.039

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Check if Makefile.PL has the right pre-requisites
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Prereq-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.40.0
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Module::Info)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 1.1.9
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Info)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

BuildArch:	noarch

%description 
The prereq_ok() function examines the modules it finds in blib/lib/,
blib/script, and the test files it finds in t/ (and test.pl). It figures out
which modules they use, skips the modules that are in the Perl core, and
compares the remaining list of modules to those in the PREREQ_PM section of
Makefile.PL.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
# this test rely on network to fetch data from CPAN
rm -f t/get_from_prereqs.t
perl -pi -e 's/get_from_prereqs.t//' t/test_manifest
%make test

%files
%doc Changes README LICENSE
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Wed Sep 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.37.0-3mdv2011.0
+ Revision: 575126
- rebuild with %%perl_convert_version

* Wed Sep 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.037-2mdv2011.0
+ Revision: 575118
- rebuild

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.037-1mdv2010.0
+ Revision: 383543
- update to new version 1.037

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.036-1mdv2009.1
+ Revision: 331593
- update to new version 1.036

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.034-1mdv2009.0
+ Revision: 279087
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.033-4mdv2009.0
+ Revision: 258577
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.033-3mdv2009.0
+ Revision: 246549
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.033-1mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Mar 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.033-1mdv2007.1
+ Revision: 147957
- drop network-dependent tests
- this is a noarch package
- Import perl-Test-Prereq

* Thu Mar 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.033-1mdv2007.1
- first mdv release


