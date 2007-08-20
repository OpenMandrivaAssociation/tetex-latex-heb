%define	texmf	/usr/share/texmf
%define	name	tetex-latex-heb
%define	version	1.0
%define	release	%mkrel 6

Summary:	Files for processing Hebrew LaTeX documents
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://linux.org.il/pub/Hebrew/HebLatex/Ivritex/Fonts/hebfonts.tar.bz2
License:	distributable
Group:		Publishing
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
URL:		http://www.dsg.technion.ac.il/heblatex/
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
משפט קצר בעברית
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

