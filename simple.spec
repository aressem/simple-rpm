Summary: A test package to see how rpmbuild works
Name: simple
Version: 0.0.1
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

