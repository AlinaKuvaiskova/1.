package calculator;

import java.util.*;
import java.util.regex.*;

public class CalculatorModel {

    public double evaluate(String expression) throws Exception {
        expression = preprocessExpression(expression);
        validateParentheses(expression);
        if (countOperands(expression) > 15)
            throw new Exception("Превышено допустимое количество слагаемых (макс. 15)");
        expression = replaceFunctions(expression);
        return evaluateExpression(expression);
    }

    private String replaceFunctions(String expr) {
        expr = expr.replaceAll("exp\\(", "exp2(");
        expr = expr.replaceAll("log\\(", "log2(");
        expr = expr.replaceAll("\\*\\*", "^");
        return expr;
    }

    private void validateParentheses(String expr) throws Exception {
        int balance = 0;
        for (char c : expr.toCharArray()) {
            if (c == '(') balance++;
            else if (c == ')') balance--;
            if (balance < 0) throw new Exception("Скобки расставлены неверно");
        }
        if (balance != 0) throw new Exception("Скобки расставлены неверно");
    }

    private int countOperands(String expr) {
        String cleaned = expr.replaceAll("[^+\\-*/^]", " ");
        return cleaned.trim().split("\\s+").length;
    }

    private double evaluateExpression(String expr) throws Exception {
        while (expr.contains("(")) {
            int close = expr.indexOf(')');
            int open = expr.lastIndexOf('(', close);
            String inner = expr.substring(open + 1, close);
            double value = evaluateFlat(inner);
            expr = expr.substring(0, open) + value + expr.substring(close + 1);
        }
        return evaluateFlat(expr);
    }

    private double evaluateFlat(String expr) throws Exception {
        // Обработка log2
        Matcher logMatcher = Pattern.compile("log2\\(([^)]+)\\)").matcher(expr);
        StringBuffer sb = new StringBuffer();
        while (logMatcher.find()) {
            double value = Math.log(Double.parseDouble(logMatcher.group(1))) / Math.log(2);
            logMatcher.appendReplacement(sb, String.valueOf(value));
        }
        logMatcher.appendTail(sb);
        expr = sb.toString();

        // Обработка exp2
        Matcher expMatcher = Pattern.compile("exp2\\(([^)]+)\\)").matcher(expr);
        sb.setLength(0); // Очистка StringBuffer
        while (expMatcher.find()) {
            double value = Math.exp(Double.parseDouble(expMatcher.group(1)));
            expMatcher.appendReplacement(sb, String.valueOf(value));
        }
        expMatcher.appendTail(sb);
        expr = sb.toString();

        // Обработка факториалов
        Pattern factPattern = Pattern.compile("(\\d+)!");
        Matcher m = factPattern.matcher(expr);
        while (m.find()) {
            int val = Integer.parseInt(m.group(1));
            expr = expr.replace(m.group(0), String.valueOf(factorial(val)));
        }

        return evaluateSimple(expr);
    }

    private double evaluateSimple(String expr) throws Exception {
        Stack<Double> values = new Stack<>();
        Stack<String> ops = new Stack<>();
        StringBuilder token = new StringBuilder();

        for (int i = 0; i < expr.length(); ) {
            char c = expr.charAt(i);
            if (Character.isWhitespace(c)) {
                i++;
                continue;
            }

            if (Character.isDigit(c) || c == '.' || (c == '-' && (i == 0 || isOperator(expr.charAt(i - 1))))) {
                token.setLength(0);
                token.append(c);
                i++;
                while (i < expr.length() && (Character.isDigit(expr.charAt(i)) || expr.charAt(i) == '.')) {
                    token.append(expr.charAt(i++));
                }
                values.push(Double.parseDouble(token.toString()));
            } else if (isOperator(c)) {
                String op = String.valueOf(c);
                i++;
                while (!ops.isEmpty() && precedence(ops.peek()) >= precedence(op)) {
                    double b = values.pop();
                    double a = values.pop();
                    values.push(applyOperator(a, b, ops.pop()));
                }
                ops.push(op);
            } else {
                throw new Exception("Неизвестный символ: " + c);
            }
        }

        while (!ops.isEmpty()) {
            double b = values.pop();
            double a = values.pop();
            values.push(applyOperator(a, b, ops.pop()));
        }

        return values.pop();
    }

    private int precedence(String op) {
        return switch (op) {
            case "^" -> 3;
            case "*", "/" -> 2;
            case "+", "-" -> 1;
            default -> 0;
        };
    }

    private double applyOperator(double a, double b, String op) throws Exception {
        return switch (op) {
            case "+" -> a + b;
            case "-" -> a - b;
            case "*" -> a * b;
            case "/" -> {
                if (b == 0) throw new Exception("Деление на ноль");
                yield a / b;
            }
            case "^" -> Math.pow(a, b);
            default -> throw new Exception("Неизвестный оператор: " + op);
        };
    }

    private int factorial(int n) throws Exception {
        if (n < 0) throw new Exception("Факториал отрицательного числа не определён");
        int result = 1;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    }

    private boolean isOperator(char c) {
        return "+-*/^".indexOf(c) >= 0;
    }

    private String preprocessExpression(String expr) {
        return expr.replaceAll("\\s+", "");
    }
}
