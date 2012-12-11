%define oname columnize

Name:       rubygem-%{oname}
Version:    0.3.1
Release:    %mkrel 1
Summary:    Read file with caching
Group:      Development/Ruby
License:    GPLv2+
URL:        http://rubyforge.org/projects/rocky-hacks/columnize
Source0:    http://rubygems.org/downloads/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Return a list of strings as a set of arranged in columns.
For example, for a line width of 4 characters (arranged vertically):
['1', '2,', '3', '4'] => '1  3
2  4
'
or arranged horizontally:
['1', '2,', '3', '4'] => '1  2
3  4
'
Each column is only as wide as necessary.  By default, columns are
separated by two spaces - one was not legible enough. Set "colsep"
to adjust the string separate columns. Set `displaywidth' to set
the line width.
Normally, consecutive items go down from the top to bottom from
the left-most column to the right-most. If +arrange_vertical+ is
set false, consecutive items will go across, left to right, top to
bottom.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/AUTHORS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/ChangeLog
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/NEWS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 623460
- import rubygem-columnize

