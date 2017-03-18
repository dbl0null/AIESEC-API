from modules import *

__UPLOADS__ = "uploads/"

class UploadsHandler(RequestHandler):

	def post(auth_token, files):

		tk = db.token.find_one({"token" : auth_token})

		if tk:
			for fl in files:
				extn = os.path.splitext(fl)[1]
				cname = str(uuid.uuid4()) + extn
				fh = open(__UPLOADS__ + cname, 'wb')
				fh.write(fl['body'])
				fh.close()
				db.users.update({"email" : tk["email"]},
					"$push" : {"files" : __UPLOADS__ + cname})

			return {"code" : 202, "status" : "successfully_uploaded"}

		else:
			return {"code" : 102, "status" : "invalid_token"}
