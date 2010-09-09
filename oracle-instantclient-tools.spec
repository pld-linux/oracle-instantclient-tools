#
# NOTE:
# - see "URL:" for download links
# - if you want to build 32-bit version, you don't have to download Source1.
#   Just comment it out.
# - if you want to build 64-bit version, comment out Source0

%define		i386rel		0.1
%define		x8664rel	0.1.0-1
Summary:	Oracle Database Workload Replay Client
Name:		oracle-instantclient-tools
Version:	11.2
Release:	0.1
License:	OTN (proprietary, non-distributable)
Group:		Applications
Source0:	instantclient-tools-linux32-%{version}.%{i386rel}.zip
# NoSource0-md5:	b63f8b6b44029775eb1a34b1d8e3d24c
Source1:	oracle-instantclient%{version}-tools-%{version}.%{x8664rel}.x86_64.zip
# NoSource1-md5:	a9d95d2500ec932837abf92802a2409f
NoSource:	0
NoSource:	1
URL:		http://www.oracle.com/technology/software/tech/oci/instantclient/index.html
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		srcdir	instantclient_%(echo %{version} | tr . _)

%description
Oracle Database Instant Client Package - WRC.
Workload Replay Client used to replay workload
for RAT's DB Replay Feature.

%prep
%ifarch %{ix86}
%setup -q -c -T -b 0
%endif

%ifarch %{x8664}
%setup -q -c -T -b 1
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{srcdir}/wrc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{srcdir}/TOOLS_README
%attr(755,root,root) %{_bindir}/wrc
