Summary:	Ruby RDF binding and mapping library
Name:		ruby-activerdf
Version:	1.6.11
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/activerdf-%{version}.gem
# Source0-md5:	1f4904cbafd17fef7ac46213eec377be
Patch0:		%{name}-nogems.patch
URL:		http://activerdf.rubyforge.org
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ActiveRDF is a library for accessing RDF data from Ruby programs. It
can be used as data layer in Ruby-on-Rails, similar to ActiveRecord
(which provides an O/R mapping to relational databases). ActiveRDF in
RoR allows you to create semantic web applications very rapidly.
ActiveRDF gives you a Domain Specific Language (DSL) for your RDF
model: you can address RDF resources, classes, properties, etc.
programmatically, without queries.

%prep
%setup -q -c -n activerdf-%{version}
tar xzf data.tar.gz
cp %{_datadir}/setup.rb .
%patch0 -p1

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

rm ri/created.rid
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/active_rdf*
%{ruby_ridir}/*
