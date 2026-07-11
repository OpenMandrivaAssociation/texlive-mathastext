%global tl_name mathastext
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4e
Release:	%{tl_revision}.1
Summary:	Use the text font in maths mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathastext
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathastext.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses a text font (usually the document's text font) for the
letters of the Latin alphabet needed when typesetting mathematics.
(Optionally, other characters in the font may also be used). This
facility makes possible (for a document with simple mathematics) a far
wider choice of text font, with little worry that no specially designed
accompanying maths fonts are available. The package also offers a simple
mechanism for using many different choices of (text hence, now, maths)
font in the same document. Of course, using one font for two purposes
helps produce smaller PDF files.

