#include <stdio.h>

int size_int;

void int_size (void) {
	unsigned int a = ~0;

	for ( size_int = 0; a != 0; ++size_int)
		a >>= 1;
}

int bitpat_search (unsigned int source, unsigned int pattern, unsigned int n) {
	int source_bit, search_bit, i, j = 0, count;
	_Bool exit = 0;

	if ( n > size_int )
		n %= size_int;
	for (i = 0; i != n; ++i ) {
		search_bit = pattern & 1 << i;
		search_bit >>= i;
		for ( ; j != size_int && exit; ++j ) {
			source_bit = source & 1 << j;
			source_bit >>= j;
			if ( source_bit == search_bit ) {
				++count;
				exit = 1;
				if ( count == n )
					return i;
			}
			else
				count = 0;
		}
	}

	return -1;
}

int main (void) {
	void int_size (void);
	int bitpat_search (unsigned int source, unsigned int pattern, unsigned int n);

	int_size ();
	printf ("%i\n", bitpat_search (0xe1f4, 0x5, 3) );

	return 0;
}