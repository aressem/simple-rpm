Summary: A test package to see how rpmbuild works
Name: simple
Version: 6.1.10
Release: 1
License: None
Group: None
Source: %{name}-%{version}.tar.gz


%description
Simple

%prep
%setup -q

%build
make tester 

%install
cp ./generated-appfile %{buildroot}/generated-appfile


%clean
rm ./generated-appfile

%files
/generated-appfile

%changelog
* Sun Jun 11 2017 Arnstein Ressem <aressem@yahoo-inc.com> 6.1.10-1
- 

* Thu Jun 08 2017 Arnstein Ressem <aressem@yahoo-inc.com> 0.0.8-1
- Setup (aressem@yahoo-inc.com)

* Thu Jun 08 2017 Arnstein Ressem <aressem@yahoo-inc.com> 0.0.7-1
- Add default source. (aressem@yahoo-inc.com)
- Add default source. (aressem@yahoo-inc.com)

* Thu Jun 08 2017 Arnstein Ressem <aressem@yahoo-inc.com> 0.0.6-1
- Simplify. (aressem@yahoo-inc.com)

* Thu Jun 08 2017 Arnstein Ressem <aressem@yahoo-inc.com> 0.0.5-1
- 

* Thu Jun 08 2017 Arnstein Ressem <aressem@yahoo-inc.com> 0.0.4-1
- 

* Thu Jun 08 2017 Arnstein Ressem <aressem@yahoo-inc.com> 0.0.3-1
- 

