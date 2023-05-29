#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - ..........................
 * @p:..................................................
 */
void print_python_float(PyObject *p)
{
	double v = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	v = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
/**
 * print_python_bytes - ....................
 * @p: ..........................................
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = 0, n = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = PyBytes_Size(p);
	printf("  size: %zd\n", s);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", s < 10 ? s + 1 : 10);
	while (n < s + 1 && n < 10)
	{
		printf(" %02hhx", str[n]);
		n++;
	}
	printf("\n");
}
/**
 * print_python_list -............................
 * @p: ,,,,,,,,,,,,,,,,,,,,,,,
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s = 0;
	PyObject *i;
	int n = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		s = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", s);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (n < s)
		{
			i = PyList_GET_ITEM(p, n);
			printf("Element %d: %s\n", n, i->ob_type->tp_name);
			if (PyBytes_Check(i))
				print_python_bytes(i);
			else if (PyFloat_Check(i))
				print_python_float(i);
			n++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
