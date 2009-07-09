%define upstream_name       forest_utils
%define upstream_version    0.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Conversion between various formats for shared derivation forest
License:	GPL
Group:		Sciences/Computer science
Url:		https://gforge.inria.fr/projects/lingwb
Source:		https://gforge.inria.fr/frs/download.php/5678/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(XML::Generator)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Data::Grove)
BuildRequires:	perl(CGI)
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
forest_utils is a set of Perl scripts to convert between various formats for
shared derivation forest produced by parsers for Tree Adjoining Grammars [TAG].

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{perl_vendorlib}/*.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE
%{_bindir}/*
%{perl_vendorlib}/Forest*
%{_mandir}/*/*

