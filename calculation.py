class CalculationHelper():
    # @classmethod
    def factors_calculations(one, variable_id):
        print("LLamada a funcion")
        print(variable_id)
        promedio = 0
        factors = Factor.objects.filter(variable__id=variable_id)
        print(factors)
        factor_serializer = FactorSerializer(factors, many=True)
        factor_data = factor_serializer.data
        factor_list = [factor['id'] for factor in factor_data]
        print(factor_list)

        for factor_id in factor_list:
            factor = "factor_{0}".format(factor_id)
            users_green = 0
            users_yellow = 0
            users_red = 0
            absence = 0

            try:
                factor_grades = collection_diagnostics.find({"factor_{0}.id".format(factor_id): factor_id})
                data = [key for key in factor_grades]
                grade_values = [key[factor]['valor'] for key in data if key['user'] in user_list]
                users_graded = len(grade_values)
                factor_name = Factor.objects.get(id=factor_id)

                for grade in grade_values:
                    if grade == 0:
                        absence += 1
                    elif 1 <= grade <= 20:
                        users_green += 1
                    elif 21 <= grade <= 65:
                        users_yellow += 1
                    elif 66 <= grade <= 100:
                        users_red += 1
                promedio += ((sum(grade_values)/(users_graded))*factor_name.weight)/100
                report_factors.append(dict({
                        "Factor": factor_name.name,
                        "Average": sum(grade_values)/users_graded,
                        "Green": (users_green*100)/users_graded,
                        "Yellow": (users_yellow*100)/users_graded,
                        "Red": (users_red*100)/users_graded,
                        "Absence": (absence*100)/users_graded
                    }))
            except:
                pass

            return report_factors, promedio
