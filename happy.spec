Vendor:       Z101-Solutions, Munich, Germany
Distribution: Softies
Name:         happy
Version:      1.7
Release:      1
Copyright:    BSD w/o adv. clause
Group:        Development/Languages/Haskell
Packager:     Sven.Panne@informatik.uni-muenchen.de
URL:          http://www.dcs.gla.ac.uk/fp/software/happy.html
Source:       ftp://ftp.dcs.gla.ac.uk:/pub/haskell/happy/happy-1.7-src.tar.gz 
Requires:     haskell
Summary:      The LALR(1) Parser Generator for Haskell
%description
This is the nth public release of our parser generator system for
Haskell, called Happy (a dyslexic acronym for 'A Yacc-like Haskell
Parser generator').  Happy is written in Haskell, uses a parser
generated by itself, and can be compiled using ghc, hbc or gofer.

The output parser can be compiled under *any* Haskell compiler,
as well as Mark Jones' Gofer interpreter.

Authors:
--------
    Simon Marlow <simonmar@microsoft.com>
    Andy Gill <andy@dcs.gla.ac.uk>

%prep
%setup -n fptools

%build
autoheader
autoconf
./configure --prefix=/usr --enable-hc-boot
make ProjectsToBuild="glafp-utils happy" WithHappyHc=ghc HC=ghc boot
make ProjectsToBuild="glafp-utils happy" WithHappyHc=ghc HC=ghc all
( cd happy/doc ; make happy.{dvi,ps,html} ; gzip -9 *.dvi *.ps )
# db2html creates the HTML subdirs with mode 700, but we want 755
chmod go+rx happy/doc/happy

%install
make ProjectsToInstall=happy install

%files
%doc happy/ANNOUNCE
%doc happy/CHANGES
%doc happy/LICENSE
%doc happy/README
%doc happy/TODO
%doc happy/doc/happy
%doc happy/doc/happy.dvi.gz
%doc happy/doc/happy.ps.gz
%doc happy/examples
/usr/bin/happy
/usr/bin/happy-1.7
/usr/lib/happy.bin
/usr/lib/happy
