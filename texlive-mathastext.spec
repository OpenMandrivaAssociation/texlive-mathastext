# revision 32415
# category Package
# catalog-ctan /macros/latex/contrib/mathastext
# catalog-date 2013-12-14 19:05:26 +0100
# catalog-license lppl1.3
# catalog-version 1.3c
Name:		texlive-mathastext
Version:	1.30c
Release:	2
Summary:	Use the text font in maths mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathastext
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses a text font (usually the document's text font)
for the letters of the Latin alphabet needed when typesetting
mathematics. (Optionally, other characters in the font may also
be used). This facility makes possible (for a document with
simple mathematics) a far wider choice of text font, with
little worry that no specially designed accompanying maths
fonts are available. The package also offers a simple mechanism
for using many different choices of (text hence, now, maths)
font in the same document. Of course, using one font for two
purposes helps produce smaller PDF files. The package, running
under LuaTeX, requires the TeX live 2013 distribution (or
later).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mathastext/mathastext.sty
%doc %{_texmfdistdir}/doc/latex/mathastext/README
%doc %{_texmfdistdir}/doc/latex/mathastext/mathastext.pdf
%doc %{_texmfdistdir}/doc/latex/mathastext/mathastext.tex
%doc %{_texmfdistdir}/doc/latex/mathastext/mathastexttestalphabets.pdf
%doc %{_texmfdistdir}/doc/latex/mathastext/mathastexttestalphabets.tex
%doc %{_texmfdistdir}/doc/latex/mathastext/mathastexttestmathversions.tex
%doc %{_texmfdistdir}/doc/latex/mathastext/mathastexttestunicodelinux.tex
%doc %{_texmfdistdir}/doc/latex/mathastext/mathastexttestunicodemacos.tex
#- source
%doc %{_texmfdistdir}/source/latex/mathastext/mathastext.dtx
%doc %{_texmfdistdir}/source/latex/mathastext/mathastext.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
