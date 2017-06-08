Summary: A test package to see how rpmbuild works
Name: simple
Version: 0.0.4
Release: 1
License: None
Group: None
Source0: testapp

%description
Simple

%prep

%build
make tester 

%install
cp ./generated-appfile %{buildroot}/generated-appfile


%clean
rm ./generated-appfile

%files
/generated-appfile

%changelog
* Thu Jun 08 2017 Arnstein Ressem <aressem@yahoo-inc.com> 0.0.4-1
- 

* Thu Jun 08 2017 Arnstein Ressem <aressem@yahoo-inc.com> 0.0.3-1
- 

