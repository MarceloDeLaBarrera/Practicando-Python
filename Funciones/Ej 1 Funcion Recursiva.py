def search_by_email_in_sf(email):
    """Busca cuenta y subcuenta por email y las retorna dentro de una lista."""

    sf_account = search_sf_account_by_email_or_id(email=email)
    #
    if sf_account is None:
        raise SalesforceNotFoundException("No se encuentra la cuenta")
    #
    sf_account_id = sf_account['records'][0]['Id']
    sf_subaccount = search_subaccount_by_id_or_name(
        sf_account_id=sf_account_id)

    if sf_subaccount['totalSize'] != 0:
        return {
            'sf_account': sf_account,
            'sf_subaccount': sf_subaccount
        }

    return None


def search_subaccount_by_id_or_name(sf_account_id=None, subaccount_name=None, sf_connection=None):
    """Busca subcuenta por su nombre o id de saleforce y la retorna."""

    if sf_connection is None:
        sf_connection = connection_salesforce()

    data = {}
    if subaccount_name != None:
        data = {
            'search': f"'{subaccount_name}'",
            'query': 'name =',
        }
    if sf_account_id != None:
        data = {
            'search': f"'{sf_account_id}'",
            'query': 'Cuenta__c =',
        }

    data_query = data['query']
    data_search = data['search']
#
    if sf_account_id != None or subaccount_name != None:
        #
        sf_subaccount = sf_connection.query(
            "SELECT name,"
            "Id,"
            "Cuenta__c,"
            "Moneda_Base__c,"
            "Estado_de_la_Subcuenta__c,"
            "Tipo_Producto__c,"
            "Producto__c,"
            "email__c"
            "FROM Subcuenta__c"
            f"WHERE {data_query} {data_search} LIMIT 200"
        )

    if sf_subaccount['totalSize'] == 0:
        return None

    return sf_subaccount


def search_sf_account_by_email_or_id(email=None, sf_account_id=None, sf_connection=None):
    """Busca cuenta por email o id de saleforce y la retorna."""

    if sf_connection is None:
        sf_connection = connection_salesforce()

    data = {}
    if email != None:
        data = {
            'search': f"'{email}'",
            'query': 'PersonEmail =',
        }
    if sf_account_id != None:
        data = {
            'search': f"'{sf_account_id}'",
            'query': 'Id =',
        }

    data_query = data['query']
    data_search = data['search']
#
    if sf_account_id != None or email != None:
        #
        sf_account = sf_connection.query(
            "SELECT Id,"
            "Name,"
            "Categoria_de_la_Cuenta__c,"
            "Subcategoria__c,"
            "Estado_del_Cliente__c,"
            "AccountNumber,"
            "PersonEmail,"
            "Producto_Real__c,"
            "Nombre_Banco1__c,"
            "Nombre_Banco2__c,"
            "Nombre_Banco3__c,"
            "Nombre_Banco4__c,"
            "Nombre_Banco5__c,"
            "Numero_Cuenta_Bancaria1__c,"
            "Numero_Cuenta_Bancaria2__c,"
            "Numero_Cuenta_Bancaria3__c,"
            "Numero_Cuenta_Bancaria4__c,"
            "Numero_Cuenta_Bancaria5__c,"
            "CCI_1__c,"
            "CCI_2__c,"
            "CCI_3__c,"
            "CCI_4__c,"
            "CCI_5__c "
            "FROM account "
            f"WHERE {data_query} {data_search} LIMIT 200")

    if sf_account['totalSize'] == 0:
        return None

    return sf_account


def calculate_commission(payment_type_id, deposit_amount):
    """Realiza el cálculo del monto de la comisión según el tipo de pago, y retorna dicho monto."""

    commission = 0
    commission_value = None

    if payment_type_id is None or deposit_amount is None:
        raise EmptyParamException("Los campos no pueden estar vacios.")

    if not isinstance(deposit_amount, (int, float)):
        raise InvalidFormatType("Tipo de formato invalido.")

    payment_type_object = PaymentType.objects.filter(id=payment_type_id)

    payment_type_object.exists == False:
        raise ObjectNotFound("El tipo de pago no existe.")

    commission = payment_type_object.commission
    commission_value = deposit_amount * commission  # TODO: Falta redondear

    return commission_value

    # Hacer funcion para obtener listado de bancos por id y name dictionario.
