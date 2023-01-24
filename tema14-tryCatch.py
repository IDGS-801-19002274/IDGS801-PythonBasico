def main():
    num1 = 20
    num2 = 0
    
    try:
        tem = num1 / num2
        print(tem)
    except ZeroDivisionError:
        print("FATAL ERROR")
    finally:
        print("No te puedes salvar de mi ejecución, sé donde vives :)")

if __name__ == '__main__':
    main()