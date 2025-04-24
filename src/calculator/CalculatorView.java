package calculator;

import java.util.Scanner;

public class CalculatorView {
    public String getExpression() {
        System.out.print("Введите выражение: ");
        Scanner scanner = new Scanner(System.in);
        return scanner.nextLine();
    }

    public void showResult(double result) {
        System.out.println("Результат: " + result);
    }

    public void showError(String message) {
        System.err.println("Ошибка: " + message);
    }
}
