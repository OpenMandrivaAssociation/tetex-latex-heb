%define	texmf	/usr/share/texmf
%define	name	tetex-latex-heb
%define	version	1.0
%define	release	%mkrel 12

Summary:	Files for processing Hebrew LaTeX documents
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://linux.org.il/pub/Hebrew/HebLatex/Ivritex/Fonts/hebfonts.tar.bz2
License:	distributable
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
URL:		https://www.dsg.technion.ac.il/heblatex/
Requires:	tetex >= 1.0.7
BuildArch:	noarch
# to have it auto-selected when choosing Hebrew at install time
Requires:	locales-he

%description
teTeX is an implementation of TeX for Linux or UNIX systems. TeX takes
a text file and a set of formatting commands as input and creates a
typesetter independent .dvi (DeVice Independent) file as output.
Usually, TeX is used in conjunction with a higher level formatting
package like LaTeX or PlainTeX, since TeX by itself is not very
user-friendly.

This package adds the fonts for hebrew support for babel/LaTeX 2e.

%prep
%setup -n hebrew
chmod 755 .

cat > README <<EOF
This package includes the following components:
* Hebrew fonts for TeX. 

The package (at least the bidi part) was authored by Boris Lavva
<lavva@tx.technion.ac.il>
it can be found at: http://www.dsg.technion.ac.il/heblatex/

This directory also contains a sample document: test-heb.tex
To test it you can try:

elatex test-heb.tex
(test-heb.dvi should be created)
xdvi test-heb

You can also find there some sample documents to test the installation 

packager: Tzafrir Cohen <tzafrir@technion.ac.il>
EOF

cat >> test-heb.tex <<EOF
\documentclass[12pt,twoside,a4paper]{article}
\usepackage[english,hebrew]{babel}
\usepackage{hebfont}
\begin{document} 
îùôè ÷öø áòáøéú
\end{document}
EOF

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{texmf}/fonts/source/hebrew
cp -p *.mf $RPM_BUILD_ROOT/%{texmf}/fonts/source/hebrew

%post 
/usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%postun
/usr/bin/env - /usr/bin/texhash 2> /dev/null
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,0755)  
%doc README test-heb.tex
%{texmf}/fonts/source/hebrew



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-12mdv2010.0
+ Revision: 434347
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-11mdv2009.0
+ Revision: 261508
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-10mdv2009.0
+ Revision: 254397
- rebuild

* Wed Feb 06 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0-8mdv2008.1
+ Revision: 162907
- rebuild because of missing i586 package
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0-7mdv2008.0
+ Revision: 70416
- use %%mkrel


* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.0-6mdk
- rebuild
- cosmetics

* Thu May 23 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0-5mdk
- Automated rebuild with gcc 3.1-1mdk

* Mon Sep 17 2001 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-4mdk
- removed .sty, .fd, .def, .fdd files (now included in babel).
- added postun.

* Fri Oct 20 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0-3mdk
- included fonts.
- updated %%post script.
- rebuilt for 7.2.

* Thu Apr 20 2000 Warly <warly@technion.ac.il> 1.0-2mdk
- change group: Publishing

* Sat Feb 05 2000 Tzafrir Cohen <tzafrir@technion.ac.il> 1.0-1mdk
- created the package. Added a README and a test doc
- adapted to MDK by Pablo Saratxaga <pablo@mandrakesoft.com>

