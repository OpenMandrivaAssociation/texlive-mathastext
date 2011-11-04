# revision 21967
# category Package
# catalog-ctan /macros/latex/contrib/mathastext
# catalog-date 2011-04-04 21:27:21 +0200
# catalog-license lppl1.3
# catalog-version 1.14c
Name:		texlive-mathastext
Version:	1.14c
Release:	1
Summary:	Use the text font in simple mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mathastext
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The mathastext package propagates the document text font to
mathematical mode, for the letters of the Latin alphabet and,
optionally, other characters in the font. Thus it makes
possible (for a document with simple mathematics) to use a
quite arbitrary text font without worrying too much that no
specially designed accompanying maths fonts are available. The
package also offers a simple mechanism for using many different
choices of (text hence, now, math) font in the same document.
Of course, using one font for two purposes helps produce
smaller PDF files.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mathastext/mathastext.sty
%doc %{_texmfdistdir}/doc/latex/mathastext/README
%doc %{_texmfdistdir}/doc/latex/mathastext/mathastext.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mathastext/mathastext.dtx
%doc %{_texmfdistdir}/source/latex/mathastext/mathastext.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
