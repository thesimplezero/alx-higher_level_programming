#include <Python.h>
#include <stdio.h>

/* Function prototype for print_python_bytes */
void print_python_bytes(PyObject *p);

/**
* print_python_list - Prints basic info about Python lists.
* @p: PyObject list
*
* Return: Nothing.
*/
void print_python_list(PyObject *p)
{
long int size, i;
PyObject *item;

printf("[*] Python list info\n");

if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
if (PyBytes_Check(item))
{
print_python_bytes(item);
}
}
}

/**
* print_python_bytes - Prints basic info about Python byte objects.
* @p: PyObject byte object
*
* Return: Nothing.
*/
void print_python_bytes(PyObject *p)
{
long int size, i;
char *trying_str;
char *item;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
trying_str = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", trying_str);

if (size < 10)
{
printf("  first %ld bytes: ", size + 1);
}
else
{
printf("  first 10 bytes: ");
size = 9;
}

item = ((PyBytesObject *)p)->ob_sval;
for (i = 0; i <= size; i++)
{
printf("%02hhx", item[i]);
if (i < size)
printf(" ");
else
printf("\n");
}
}
