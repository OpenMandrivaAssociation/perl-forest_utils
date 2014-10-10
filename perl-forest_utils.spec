%define upstream_name       forest_utils
%define upstream_version    0.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Conversion between various formats for shared derivation forest
License:	GPL
Group:		Sciences/Computer science
Url:		https://gforge.inria.fr/projects/lingwb
Source:		https://gforge.inria.fr/frs/download.php/5678/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Generator)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Data::Grove)
BuildRequires:	perl(CGI)
BuildRequires:	perl(AppConfig)
BuildArch:	noarch

%description
forest_utils is a set of Perl scripts to convert between various formats for
shared derivation forest produced by parsers for Tree Adjoining Grammars [TAG].

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/*.pl

%files
%doc ChangeLog INSTALL LICENSE
%{_bindir}/*
%{perl_vendorlib}/Forest*
%{_mandir}/*/*

%changelog
* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 393851
- new version
- use %%perl_convert_version macro

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-5mdv2009.0
+ Revision: 241224
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-3mdv2008.0
+ Revision: 86407
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-2mdv2007.0
- Rebuild

* Mon Mar 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdk
- new version

* Fri Mar 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdk
- buildrequires

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- new version
- drop patches

* Fri Dec 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-5mdk
- fixed name

* Fri Dec 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-4mdk
- spec cleanup
- %%mkrel

* Wed Dec 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.05-3mdk 
- fix buildrequires in a backward compatible way

* Mon Nov 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.05-2mdk 
- fix namespace issues

* Tue Nov 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.05-1mdk 
- first mdk release

