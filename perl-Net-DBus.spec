#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-DBus
Version  : 1.1.0
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Net-DBus-1.1.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DANBERR/Net-DBus-1.1.0.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-2.0 GPL-2.0+
Requires: perl-Net-DBus-lib = %{version}-%{release}
Requires: perl-Net-DBus-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : dbus-dev
BuildRequires : perl(Test::CPAN::Changes)
BuildRequires : perl(Test::Pod)
BuildRequires : perl(Test::Pod::Coverage)
BuildRequires : perl(XML::Parser)
BuildRequires : perl(XML::Twig)

%description
Net::DBus provides a Perl API for the DBus message system. The DBus Perl
interface is currently operating against the 0.33 development version of
DBus, but should work with later versions too, providing the API changes
have not been too drastic.

%package dev
Summary: dev components for the perl-Net-DBus package.
Group: Development
Requires: perl-Net-DBus-lib = %{version}-%{release}
Provides: perl-Net-DBus-devel = %{version}-%{release}

%description dev
dev components for the perl-Net-DBus package.


%package lib
Summary: lib components for the perl-Net-DBus package.
Group: Libraries
Requires: perl-Net-DBus-license = %{version}-%{release}

%description lib
lib components for the perl-Net-DBus package.


%package license
Summary: license components for the perl-Net-DBus package.
Group: Default

%description license
license components for the perl-Net-DBus package.


%prep
%setup -q -n Net-DBus-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-DBus
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Net-DBus/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/ASyncReply.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Annotation.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/BaseObject.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Bus.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Connection.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Introspector.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Iterator.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Message.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Message/Error.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Message/MethodCall.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Message/MethodReturn.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Message/Signal.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/PendingCall.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Server.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Value.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Binding/Watch.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Callback.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Dumper.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Error.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Exporter.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Object.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/ProxyObject.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Reactor.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/RemoteObject.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/RemoteService.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Service.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Test/MockConnection.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Test/MockIterator.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Test/MockMessage.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Test/MockObject.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Tutorial.pod
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Tutorial/ExportingObjects.pod
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Net/DBus/Tutorial/UsingObjects.pod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::DBus.3
/usr/share/man/man3/Net::DBus::ASyncReply.3
/usr/share/man/man3/Net::DBus::Annotation.3
/usr/share/man/man3/Net::DBus::BaseObject.3
/usr/share/man/man3/Net::DBus::Binding::Bus.3
/usr/share/man/man3/Net::DBus::Binding::Connection.3
/usr/share/man/man3/Net::DBus::Binding::Introspector.3
/usr/share/man/man3/Net::DBus::Binding::Iterator.3
/usr/share/man/man3/Net::DBus::Binding::Message.3
/usr/share/man/man3/Net::DBus::Binding::Message::Error.3
/usr/share/man/man3/Net::DBus::Binding::Message::MethodCall.3
/usr/share/man/man3/Net::DBus::Binding::Message::MethodReturn.3
/usr/share/man/man3/Net::DBus::Binding::Message::Signal.3
/usr/share/man/man3/Net::DBus::Binding::PendingCall.3
/usr/share/man/man3/Net::DBus::Binding::Server.3
/usr/share/man/man3/Net::DBus::Binding::Value.3
/usr/share/man/man3/Net::DBus::Binding::Watch.3
/usr/share/man/man3/Net::DBus::Callback.3
/usr/share/man/man3/Net::DBus::Dumper.3
/usr/share/man/man3/Net::DBus::Error.3
/usr/share/man/man3/Net::DBus::Exporter.3
/usr/share/man/man3/Net::DBus::Object.3
/usr/share/man/man3/Net::DBus::ProxyObject.3
/usr/share/man/man3/Net::DBus::Reactor.3
/usr/share/man/man3/Net::DBus::RemoteObject.3
/usr/share/man/man3/Net::DBus::RemoteService.3
/usr/share/man/man3/Net::DBus::Service.3
/usr/share/man/man3/Net::DBus::Test::MockConnection.3
/usr/share/man/man3/Net::DBus::Test::MockIterator.3
/usr/share/man/man3/Net::DBus::Test::MockMessage.3
/usr/share/man/man3/Net::DBus::Test::MockObject.3
/usr/share/man/man3/Net::DBus::Tutorial.3
/usr/share/man/man3/Net::DBus::Tutorial::ExportingObjects.3
/usr/share/man/man3/Net::DBus::Tutorial::UsingObjects.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Net/DBus/DBus.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-DBus/LICENSE
