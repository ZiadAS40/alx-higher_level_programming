#include <Python.h>

/**
 * print_python_list_info - prints a some basic information
 * about Python lists
 * @p: a PyObject pointer
 */

void print_python_list_info(PyObject *p)
{
    const char *elType;
    PyObject *el;
    Py_ssize_t py_size = PyList_Size(p), i;
    Py_ssize_t alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", py_size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < py_size; i++)
    {
        el = PyList_GetItem(p, i);
        elType = Py_TYPE(el)->tp_name;

        printf("Element %ld: %s\n", i, elType);
    }
}
