Name:		bwa
Version:	0.6.1
Release:	1
Summary:	Burrows-Wheeler Alignment tool

Group:		Sciences/Biology
License:	GPLv3
URL:		http://bio-bwa.sourceforge.net/
Source0:	http://downloads.sourceforge.net/bio-%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	zlib-devel
Patch0:		msse2_makefile.patch

%description

BWA is a program for aligning sequencing reads against a large
reference genome (e.g. human genome). It has two major components, one
for read shorter than 150bp and the other for longer reads.

%prep
%setup -q
%patch0 -p0


%build

%make

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1

install -m 0755 bwa %{buildroot}/%{_bindir}
install -m 0755 solid2fastq.pl %{buildroot}/%{_bindir}
install -m 0755 qualfa2fq.pl %{buildroot}/%{_bindir}
install -m 0644 bwa.1 %{buildroot}/%{_mandir}/man1/bwa.1

%files
%doc COPYING NEWS 
%{_mandir}/man1/%{name}.1*
%{_bindir}/bwa
%{_bindir}/qualfa2fq.pl
%{_bindir}/solid2fastq.pl
