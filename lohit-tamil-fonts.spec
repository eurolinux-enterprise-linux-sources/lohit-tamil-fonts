%global fontname lohit-tamil
%global fontconf 65-0-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.5.3
Release:        1%{?dist}
Summary:        Free Tamil font

Group:          User Interface/X
License:        OFL
URL:            https://fedorahosted.org/lohit/
Source0:        https://fedorahosted.org/releases/l/o/lohit/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Tamil truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version}
mv 66-lohit-tamil.conf 65-0-lohit-tamil.conf


%build
make

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README ChangeLog.old


%changelog
* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolves bug 829143

* Wed Jun 06 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream release 2.5.1

* Thu May 10 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.0-3
- Resolves bug 820478

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-7
- fixed bug 673419, asterisk character and rupee sign

* Thu Sep 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-6
- improved fixe to bug 629824, punctuations marks

* Fri Sep 10 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-5
- fixed bug 629824, punctuations mark size

* Wed Aug 23 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- fixed bug 621445, conf file

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- fixed bug 578039, conf file

* Thu Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- fixed bug 548686, license field

* Tue Nov 24 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release

* Wed Nov 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- resolved rh bug 536724

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball
