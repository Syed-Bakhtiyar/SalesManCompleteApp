from flask import request, jsonify
from services.company import createCompany, getAllCompanies, updateCompany, deleteCompany

def company(app):
    @app.route('/admin/company', methods=['POST'])
    def addCompany():
        try:
            adminId = request.form['adminId']
            name = request.form['name']
            company = createCompany(adminId,name);
            return jsonify(company), 200
        except Exception as error:
            print(error)
            return jsonify({'message': 'internal server error'}), 500


    @app.route('/admin/<admin_id>/company')
    def getCompanies(admin_id):
        try:
            print(admin_id)
            company = getAllCompanies(admin_id);
            if 'status' in company.keys() :
                if company['status'] == 404:
                    return jsonify({'message': company['message']}), 404
                if company['status'] == 500:
                    raise Exception
            return jsonify(company), 200
        except Exception as error:
            print(error)
            return jsonify({'message': 'internal server error'}), 500

    # post means update not create
    @app.route('/admin/company/<company_id>/action', methods=['POST', 'DELETE'])
    def modifyCompany(company_id):
        if request.method == 'POST':
            try:
                name = request.form['name']
                company = updateCompany(company_id, name);
                if 'status' in company.keys() :
                    if company['status'] == 404:
                        return jsonify({'message': company['message']}), 404
                    if company['status'] == 500:
                        raise Exception
                return jsonify(company), 200
            except Exception as error:
                print(error)
                return jsonify({'message': 'internal server error'}), 500

        if request.method == 'DELETE':
            try:
                company = deleteCompany(company_id);
                if 'status' in company.keys() :
                    if company['status'] == 404:
                        return jsonify({'message': company['message']}), 404
                    if company['status'] == 500:
                        raise Exception
                return jsonify(company), 200
            except Exception as error:
                print(error)
                return jsonify({'message': 'internal server error'}), 500
        else:
            return jsonify({'message': 'Bad Request Method'}), 400