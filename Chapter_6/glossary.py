glossary = {
    'c':'The GNU Compiler Collection (GCC) is a collection of compilers from \
the GNU Project that support various programming languages, \
hardware architectures and operating systems.',
    'rust':'Rust is a general-purpose programming language emphasizing perfo\
rmance, type safety, and concurrency. It enforces memory safety, \
meaning that all references point to valid memory.',
    'python':'Python is a high-level, general-purpose programming language. \
Its design philosophy emphasizes code readability with the use of \
significant indentation.',
    'computer science':'Computer science is the study of computation, \
information, and automation. Computer science spans theoretical \
disciplines (such as algorithms, theory of computation, and \
information theory) to applied disciplines (including the \
design and implementation of hardware and software).',
    'deep learning':'Deep learning is a subset of machine learning methods \
based on neural networks with representation learning. The field takes \
inspiration from biological neuroscience and is centered around \
stacking artificial neurons into layers and "training" them \
to process data. The adjective "deep" refers to the use \
of multiple layers (ranging from three to several \
hundred or thousands) in the network. Methods \
used can be either supervised, semi-supervised\
or unsupervised.',
}

for k, v in glossary.items():
    print(f'\n{k.title()}:{v}')